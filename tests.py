'''
Gitea Auto Updater

Copyright 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import gitea_auto_update.lib.version
import unittest

version = gitea_auto_update.lib.version.Version('', '')

class Tests(unittest.TestCase):

    def testSimpleVersion(self):
        self.assertTrue(version.checkVersion('1.9.1', '1.9.0'))

    def testTwoIntVersion(self):
        self.assertTrue(version.checkVersion('1.10.0', '1.9.0'))

    def testFalseVersion(self):
        self.assertFalse(version.checkVersion('1.8.0', '1.9.0'))

    def testSameVersion(self):
        self.assertFalse(version.checkVersion('1.9.7', '1.9.7'))

    def testInt(self):
        self.assertTrue(version.checkVersion('9', '8'))

    def testSuffix(self):
        self.assertTrue(version.checkVersion('1.9.0+dev-264-g8de76b6e6', '1.8.0'))

    def testParseFileVersion(self):
        self.assertEqual(version.parseFileVersion('Gitea version 1.8.1 built with go1.12.2 : bindata, sqlite, sqlite_unlock_notify'), '1.8.1')

if __name__ == '__main__':
    unittest.main()