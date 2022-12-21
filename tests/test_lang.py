import os
import glob
import string
import unittest
from amulet_map_editor.api.lang import lang_dirs


KeyCharacterSet = set(string.ascii_lowercase + string.digits + "_.")


class LangTestCase(unittest.TestCase):
    def test_lang(self):
        for lang_dir in lang_dirs():
            for lang_path in glob.glob(os.path.join(glob.escape(lang_dir), "*")):
                self.assertTrue(
                    lang_path.endswith(".lang"),
                    f'{lang_path} does not end with ".lang".',
                )
                self.assertTrue(
                    os.path.isfile(lang_path), f"{lang_path} is not a file."
                )
                with open(lang_path, encoding="utf-8") as f:
                    unique_ids = set()
                    for line_number, line in enumerate(f.readlines()):
                        line_number += 1
                        strip_line = line.strip()
                        if strip_line and not strip_line.startswith("#"):
                            split_line = line.split("=", 1)
                            self.assertEqual(
                                len(split_line),
                                2,
                                f"{lang_path} line {line_number}: No = symbol present.",
                            )
                            unique_identifier = split_line[0].strip()
                            self.assertTrue(
                                len(unique_identifier) > 0,
                                f"{lang_path} line {line_number}: There is no identifier before the first = symbol.",
                            )
                            self.assertTrue(
                                set(unique_identifier).issubset(KeyCharacterSet),
                                f"{lang_path} line {line_number}: identifier is not a subset of a-z0-9_.",
                            )
                            self.assertTrue(
                                unique_identifier not in unique_ids,
                                f"{lang_path} line {line_number}: identifier already defined in the file.",
                            )
                            unique_ids.add(unique_identifier)
                            language_string = split_line[1].replace("\\n", "\n").strip()
                            self.assertTrue(
                                len(language_string) > 0,
                                f"{lang_path} line {line_number}: There is no translation string after the first = symbol.",
                            )


if __name__ == "__main__":
    unittest.main()
