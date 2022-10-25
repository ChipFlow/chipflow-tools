from src.base import SourceLocation, Target

SourceLocation(
	name = 'migen',
	vcs = 'git',
	location = 'https://github.com/m-labs/migen',
	revision = 'origin/master',
	license_file = 'LICENSE',
)

Target(
	name = 'migen',
	sources = [ 'migen' ],
	dependencies = [ 'python3' ],
	resources = [ 'python3' ],
	patches = [ 'python3_package.sh' ],
)
