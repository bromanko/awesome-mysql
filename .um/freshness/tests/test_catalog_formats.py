"""Catalog-format boundaries: metadata and existing list styles are preserved."""
import hashlib
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import ci
import catalog

class CatalogFormatTests(unittest.TestCase):
    def proposal(self, text, **changes):
        data=dict(catalogSha='a'*40,readme=text,readmeHash=hashlib.sha256(text.encode()).hexdigest(),entries=ci.entries(text))
        row=dict(id=data['entries'][0]['id'],action='update',reason='Verified correction.',evidence=[dict(url='https://example.com',observation='Official source.')],limitations=[],blockers=[],newName=None,newUrl=None,newDescription=None)
        row.update(changes)
        return ci.previews(data,dict(results=[row]),'unchanged')[0]

    def test_indented_bullet_is_preserved(self):
        proposal=self.proposal('# Tools\n  * [Tool](https://example.com) - Old.\n',newDescription='New.')
        self.assertIn('+  * [Tool](https://example.com) - New.',proposal[0]['patch'])

    def test_missing_dash_separator_is_preserved(self):
        proposal=self.proposal('# Tools\n  * [Tool](https://example.com) Old.\n',newDescription='New.')
        self.assertIn('+  * [Tool](https://example.com) New.',proposal[0]['patch'])

    def test_bare_links_are_researched_and_url_can_change(self):
        proposal=self.proposal('# General\n- [Tool](https://example.com)\n',newUrl='https://new.example')
        self.assertIn('+\u002d [Tool](https://new.example)\n',proposal[0]['patch'])
        self.assertNotIn(' - ',proposal[0]['patch'])

    def test_archived_annotation_survives(self):
        proposal=self.proposal('# Tools\n- [Tool](https://example.com) (archived) - Old.\n',newDescription='New.')
        self.assertIn('+\u002d [Tool](https://example.com) (archived) - New.',proposal[0]['patch'])

    def test_multiple_identity_links_hold_edit(self):
        self.assertEqual([],self.proposal('# Tools\n- [Parent](https://example.com)/[Child](https://example.com/child) - Old.\n',newDescription='New.'))

    def test_metadata_change_invalidates_claim(self):
        a=ci.entries('# Tools\n- [Tool](https://example.com) - Old.')[0]
        b=ci.entries('# Tools\n- [Tool](https://example.com) (archived) - Old.')[0]
        self.assertNotEqual(catalog.claim(a,''),catalog.claim(b,''))

    def test_current_catalog_has_full_coverage(self):
        import re
        text=Path('README.md').read_text()
        expected=len(re.findall(r'^\s*[-*+] .*\]\(https?://',text,re.M))
        self.assertEqual(len(ci.entries(text)),expected)
        self.assertFalse(re.search(r'^\|.*https?://',text,re.M))

    def test_navigation_links_are_not_entries(self):
        rows=ci.entries('# Contents\n- [Tools](#tools)\n# Tools\n- [Tool](https://example.com)\n')
        self.assertEqual(len(rows),1)

    def test_compound_identity_watches_both_sources(self):
        from unittest.mock import patch
        entry=ci.entries('- [Parent](https://example.com)/[Child](https://child.example) - Tool.')[0]
        with patch.object(catalog, 'source_snapshot', side_effect=lambda e: dict(complete=True,source={'url':e['url']})) as fetch:
            value=catalog.snapshot(entry)
        self.assertTrue(value['complete'])
        self.assertEqual(fetch.call_count,2)
        self.assertEqual(value['source']['sources'][1]['url'],'https://child.example')

    def test_description_must_preserve_companion_links(self):
        text='# Tools\n- [Parent](https://example.com) - Uses [Child](https://child.example).\n'
        self.assertEqual([],self.proposal(text,newDescription='Tool.'))
        self.assertEqual(1,len(self.proposal(text,newDescription='Supports [Child](https://child.example).')))

    def test_removal_does_not_orphan_nested_content(self):
        text='# Tools\n- [Parent](https://example.com) - Tool.\n\n  More information about the tool.\n'
        self.assertEqual([],self.proposal(text,action='remove'))

    def test_url_only_update_preserves_existing_name_and_whitespace(self):
        text='# Tools\n- [Tool (Legacy)](https://example.com) - Description.  \n'
        proposal=self.proposal(text,newUrl='https://new.example')
        self.assertIn('+\u002d [Tool (Legacy)](https://new.example) - Description.  \n',proposal[0]['patch'])

    def test_companion_destination_requires_success(self):
        import checks
        entry=ci.entries('- [Tool](https://example.com) - [Docs](https://docs.example).')[0]
        result=checks.compare_links(dict(errors=[]),dict(errors=[],excluded=['https://docs.example'],successful=['https://example.com']),ci.linked_urls(entry))
        self.assertFalse(result['passed'])
