import sys
import pytest
from errata_tool.cli import main
from errata_tool.release import NoReleaseFoundError


class FakeRelease(object):
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = 'Foo description'
        self.url = 'https://errata.devel.redhat.com/myrelease'
        self.edit_url = 'https://errata.devel.redhat.com/myrelease/edit'


class FakeMissingRelease(object):
    def __init__(self, **kwargs):
        raise NoReleaseFoundError

    @classmethod
    def create(cls, **kwargs):
        name = kwargs['name']
        return FakeRelease(name=name)


def test_short_help(monkeypatch):
    argv = ['errata-tool', 'release', '-h']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_help(monkeypatch):
    argv = ['errata-tool', 'release', '--help']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_get_missing_name(monkeypatch):
    argv = ['errata-tool', 'release', 'get']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_get(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeRelease)
    argv = ['errata-tool', 'release', 'get', 'foo-3.0']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()


def test_get_missing(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'get', 'missing-3.0']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_create_missing_args(monkeypatch):
    argv = ['errata-tool', 'release', 'create']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_create_ystream_missing_args(monkeypatch):
    argv = ['errata-tool', 'release', 'create', 'ystream']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_create_ystream(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'ystream',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--program_manager', 'anharris',
            '--blocker_flags', 'ceph-2.y',
            '--default_brew_tag', 'ceph-3.0-rhel-7-candidate']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()


def test_create_ystream_missing_blocker(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'ystream',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--program_manager', 'anharris',
            '--default_brew_tag', 'ceph-3.0-rhel-7-candidate']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_create_ystream_missing_default_brew_tag(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'ystream',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--program_manager', 'anharris',
            '--blocker_flags', 'ceph-2.y']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()


def test_create_ystream_missing_program_manager(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'ystream',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--blocker_flags', 'ceph-2.y',
            '--default_brew_tag', 'ceph-3.0-rhel-7-candidate']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()


def test_create_zstream_missing_args(monkeypatch):
    argv = ['errata-tool', 'release', 'create', 'zstream']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_create_zstream(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'zstream',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--program_manager', 'anharris',
            '--blocker_flags', 'ceph-2.y',
            '--default_brew_tag', 'ceph-3.0-rhel-7-candidate']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()


def test_create_zstream_missing_blocker(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'zstream',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--program_manager', 'anharris',
            '--default_brew_tag', 'ceph-3.0-rhel-7-candidate']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_create_zstream_missing_default_brew_tag(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'zstream',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--program_manager', 'anharris',
            '--blocker_flags', 'ceph-2.y']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()


def test_create_zstream_missing_program_manager(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'zstream',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--blocker_flags', 'ceph-2.y',
            '--default_brew_tag', 'ceph-3.0-rhel-7-candidate']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()


def test_create_async_missing_args(monkeypatch):
    argv = ['errata-tool', 'release', 'create', 'async']
    monkeypatch.setattr(sys, 'argv', argv)
    with pytest.raises(SystemExit):
        main.main()


def test_create_async(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'async',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--program_manager', 'anharris',
            '--default_brew_tag', 'ceph-3.0-rhel-7-candidate']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()


def test_create_async_missing_default_brew_tag(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'async',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--program_manager', 'anharris',
            '--blocker_flags', 'ceph-2.y']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()


def test_create_async_missing_program_manager(monkeypatch):
    monkeypatch.setattr('errata_tool.cli.release.Release', FakeMissingRelease)
    argv = ['errata-tool', 'release', 'create', 'async',
            '--name', 'rhceph-2.4',
            '--product', 'RHCEPH',
            '--product_version', 'RHEL-7-CEPH-2',
            '--default_brew_tag', 'ceph-3.0-rhel-7-candidate']
    monkeypatch.setattr(sys, 'argv', argv)
    main.main()
