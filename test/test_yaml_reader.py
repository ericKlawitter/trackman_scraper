import yaml_reader
from unittest import TestCase


class TestYamlReader(TestCase):

    def test_get_config(self):
        config = yaml_reader.get_config("resources/test_yaml.yaml")
        self.assertTrue('config' in config)
        config_yaml = config['config']
        self.assertEqual(1, len(config_yaml))
        foo = config_yaml[0]
        self.assertTrue('foo' in foo)
        self.assertEqual(2, len(foo['foo']))
        self.assertEqual('py', foo['foo'][0])
        self.assertEqual('none', foo['foo'][1])

    def test_get_config_yaml_ex(self):
        with self.assertRaises(Exception) as ctx:
            t = yaml_reader.get_config("resources/malformed_yaml.yaml")
        self.assertTrue('error loading yaml' in str(ctx.exception))

    def test_get_config_nonexistent(self):
        try:
            t = yaml_reader.get_config("nonexistent.yaml")
            self.fail('exception not thrown')
        except FileNotFoundError:
            pass
