from src.base import SourceLocation, Target

# HDL
SourceLocation(
	name = 'amaranth',
	vcs = 'git',
	location = 'https://github.com/amaranth-lang/amaranth',
	revision = 'origin/main',
	license_file = 'LICENSE.txt',
)

SourceLocation(
	name = 'amaranth-boards',
	vcs = 'git',
	location = 'https://github.com/amaranth-lang/amaranth-boards',
	revision = 'origin/main',
	license_file = 'LICENSE.txt',
)

SourceLocation(
	name = 'amaranth-soc',
	vcs = 'git',
	location = 'https://github.com/amaranth-lang/amaranth-boards',
	revision = 'origin/main',
	license_file = 'LICENSE.txt',
)

SourceLocation(
	name = 'amaranth-stdio',
	vcs = 'git',
	location = 'https://github.com/amaranth-lang/amaranth-boards',
	revision = 'origin/main',
	license_file = 'LICENSE.txt',
)

SourceLocation(
        name = 'amaranth-vexriscv',
        vcs = 'git',
        location = 'https://gitlab.com/ChipFlow/amaranth-vexriscv.git',
        revision = 'origin/main',
        license_file = 'LICENSE.txt',
)

SourceLocation(
        name = 'amaranth-orchard',
        vcs = 'git',
        location = 'https://gitlab.com/ChipFlow/amaranth-orchard.git',
        revision = 'origin/main',
        license_file = 'LICENSE.txt',
)

Target(
	name = 'amaranth',
	sources = [ 'amaranth', 'amaranth-boards', 'amaranth-soc',
            'amaranth-stdio', 'amaranth-vexriscv', 'amaranth-orchard' ],
	dependencies = [ 'python3' ],
	resources = [ 'python3' ],
	patches = [ 'python3_package.sh' ],
)
