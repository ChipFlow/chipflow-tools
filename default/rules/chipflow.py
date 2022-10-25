from src.base import Target

Target(
    name = 'chipflow',
    release_name = 'chipflow-tools',
    top_package = True,
    dependencies = [
        'yosys',
        'nextpnr-generic',
        'nextpnr-ice40',
        'nextpnr-ecp5',
        'nextpnr-machxo2',
        'nextpnr-nexus',
        'icestorm',
        'prjtrellis',
        'prjoxide',
        'dfu-util',
        'ecpprog',
        'openfpgaloader',
        'gtkwave',
        'ecpdap',
        'fujprog',
        'iceprogduino',
        'python-programmers',
        'openocd',
        'icesprog',
        'utils',
        'amaranth',
    ],
    branding = 'ChipFlow Tools',
    readme = 'README.ChipFlow',
    resources = [ 'system-resources' ],
)

