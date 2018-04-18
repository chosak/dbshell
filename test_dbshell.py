import os
import subprocess
import unittest


COMMAND = './dbshell'


class CommandTests(unittest.TestCase):
    def run_command(self, database_url=None, env={}, stdin=None):
        testenv = os.environ.copy()
        testenv.update(env)

        args = [database_url] if database_url else []

        process = subprocess.Popen(
            [COMMAND] + args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=testenv,
            universal_newlines=True
        )

        out, err = process.communicate(input=stdin)

        return out, err

    def test_comand_no_arguments_only_writes_to_stderr(self):
        out, err = self.run_command()
        self.assertFalse(out)
        self.assertTrue(err)

    def test_command_no_arguments_mentions_required_env_variable(self):
        out, err = self.run_command()
        self.assertIn('DATABASE_URL', err)

    def check_command_with_invalid_url_only_writes_to_stderr(self, **kwargs):
        out, err = self.run_command(**kwargs)
        self.assertFalse(out)
        self.assertTrue(err)

    def test_command_with_invalid_argument_url_only_writes_to_stderr(self):
        self.check_command_with_invalid_url_only_writes_to_stderr(
            database_url='invalid url'
        )

    def test_command_with_invalid_env_url_only_writes_to_stderr(self):
        self.check_command_with_invalid_url_only_writes_to_stderr(
            env={'DATABASE_URL': 'invalid url'}
        )

    def check_command_with_valid_url_generates_expected_output(self, **kwargs):
        out, err = self.run_command(stdin='SELECT 1 + 1;', **kwargs)
        self.assertEqual(out, '2\n')
        self.assertFalse(err)

    def test_command_with_valid_argument_url_generates_expected_output(self):
        self.check_command_with_valid_url_generates_expected_output(
            database_url='sqlite://:memory:',
        )

    def test_command_with_valid_env_url_generates_expected_output(self):
        self.check_command_with_valid_url_generates_expected_output(
            env={'DATABASE_URL': 'sqlite://:memory:'}
        )


if __name__ == '__main__':
    unittest.main()
