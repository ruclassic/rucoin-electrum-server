from setuptools import setup

setup(
    name="electrum-ruc-server",
    version="0.9",
    scripts=['run_electrum_ruc_server','electrum-ruc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumrucserver':'src'
        },
    py_modules=[
        'electrumrucserver.__init__',
        'electrumrucserver.utils',
        'electrumrucserver.storage',
        'electrumrucserver.deserialize',
        'electrumrucserver.networks',
        'electrumrucserver.blockchain_processor',
        'electrumrucserver.server_processor',
        'electrumrucserver.processor',
        'electrumrucserver.version',
        'electrumrucserver.ircthread',
        'electrumrucserver.stratum_tcp',
        'electrumrucserver.stratum_http'
    ],
    description="RUcoin Electrum Server",
    author="Thomas Voegtlin & Sunerok",
    author_email="thomasv1@gmx.de",
    license="MIT",
    url="https://github.com/ruclassic/rucoin-electrum-server",
    long_description="""Server for the Electrum Lightweight RUcoin Wallet"""
)


