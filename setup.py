from setuptools import setup

setup(
    name='find_cheapest_flight',
    version='v0.0.1',
    packages=['', 'venv.Lib.site-packages.bs4', 'venv.Lib.site-packages.bs4.tests',
              'venv.Lib.site-packages.bs4.builder', 'venv.Lib.site-packages.pip', 'venv.Lib.site-packages.pip._vendor',
              'venv.Lib.site-packages.pip._vendor.idna', 'venv.Lib.site-packages.pip._vendor.pep517',
              'venv.Lib.site-packages.pip._vendor.pytoml', 'venv.Lib.site-packages.pip._vendor.certifi',
              'venv.Lib.site-packages.pip._vendor.chardet', 'venv.Lib.site-packages.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip._vendor.distlib', 'venv.Lib.site-packages.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip._vendor.msgpack', 'venv.Lib.site-packages.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip._vendor.urllib3.util', 'venv.Lib.site-packages.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip._vendor.colorama', 'venv.Lib.site-packages.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treebuilders', 'venv.Lib.site-packages.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip._vendor.progress', 'venv.Lib.site-packages.pip._vendor.requests',
              'venv.Lib.site-packages.pip._vendor.packaging', 'venv.Lib.site-packages.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip._vendor.webencodings', 'venv.Lib.site-packages.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip._internal', 'venv.Lib.site-packages.pip._internal.cli',
              'venv.Lib.site-packages.pip._internal.req', 'venv.Lib.site-packages.pip._internal.vcs',
              'venv.Lib.site-packages.pip._internal.utils', 'venv.Lib.site-packages.pip._internal.models',
              'venv.Lib.site-packages.pip._internal.commands', 'venv.Lib.site-packages.pip._internal.operations',
              'venv.Lib.site-packages.zmq', 'venv.Lib.site-packages.zmq.log', 'venv.Lib.site-packages.zmq.ssh',
              'venv.Lib.site-packages.zmq.auth', 'venv.Lib.site-packages.zmq.auth.asyncio',
              'venv.Lib.site-packages.zmq.green', 'venv.Lib.site-packages.zmq.green.eventloop',
              'venv.Lib.site-packages.zmq.sugar', 'venv.Lib.site-packages.zmq.tests',
              'venv.Lib.site-packages.zmq.tests.asyncio', 'venv.Lib.site-packages.zmq.utils',
              'venv.Lib.site-packages.zmq.asyncio', 'venv.Lib.site-packages.zmq.backend',
              'venv.Lib.site-packages.zmq.backend.cffi', 'venv.Lib.site-packages.zmq.backend.cython',
              'venv.Lib.site-packages.zmq.devices', 'venv.Lib.site-packages.zmq.eventloop',
              'venv.Lib.site-packages.zmq.eventloop.minitornado',
              'venv.Lib.site-packages.zmq.eventloop.minitornado.platform', 'venv.Lib.site-packages.cffi',
              'venv.Lib.site-packages.idna', 'venv.Lib.site-packages.jedi', 'venv.Lib.site-packages.jedi.api',
              'venv.Lib.site-packages.jedi.common', 'venv.Lib.site-packages.jedi.evaluate',
              'venv.Lib.site-packages.jedi.evaluate.context', 'venv.Lib.site-packages.jedi.evaluate.compiled',
              'venv.Lib.site-packages.jedi.evaluate.compiled.subprocess', 'venv.Lib.site-packages.past',
              'venv.Lib.site-packages.past.tests', 'venv.Lib.site-packages.past.types',
              'venv.Lib.site-packages.past.utils', 'venv.Lib.site-packages.past.builtins',
              'venv.Lib.site-packages.past.translation', 'venv.Lib.site-packages.poyo', 'venv.Lib.site-packages.arrow',
              'venv.Lib.site-packages.click', 'venv.Lib.site-packages.parso', 'venv.Lib.site-packages.parso.pgen2',
              'venv.Lib.site-packages.parso.python', 'venv.Lib.site-packages.future',
              'venv.Lib.site-packages.future.moves', 'venv.Lib.site-packages.future.moves.dbm',
              'venv.Lib.site-packages.future.moves.html', 'venv.Lib.site-packages.future.moves.http',
              'venv.Lib.site-packages.future.moves.test', 'venv.Lib.site-packages.future.moves.urllib',
              'venv.Lib.site-packages.future.moves.xmlrpc', 'venv.Lib.site-packages.future.moves.tkinter',
              'venv.Lib.site-packages.future.tests', 'venv.Lib.site-packages.future.types',
              'venv.Lib.site-packages.future.utils', 'venv.Lib.site-packages.future.builtins',
              'venv.Lib.site-packages.future.backports', 'venv.Lib.site-packages.future.backports.html',
              'venv.Lib.site-packages.future.backports.http', 'venv.Lib.site-packages.future.backports.test',
              'venv.Lib.site-packages.future.backports.email', 'venv.Lib.site-packages.future.backports.email.mime',
              'venv.Lib.site-packages.future.backports.urllib', 'venv.Lib.site-packages.future.backports.xmlrpc',
              'venv.Lib.site-packages.future.standard_library', 'venv.Lib.site-packages.jinja2',
              'venv.Lib.site-packages.tinydb', 'venv.Lib.site-packages.certifi', 'venv.Lib.site-packages.chardet',
              'venv.Lib.site-packages.chardet.cli', 'venv.Lib.site-packages.IPython',
              'venv.Lib.site-packages.IPython.lib', 'venv.Lib.site-packages.IPython.lib.tests',
              'venv.Lib.site-packages.IPython.core', 'venv.Lib.site-packages.IPython.core.tests',
              'venv.Lib.site-packages.IPython.core.magics', 'venv.Lib.site-packages.IPython.utils',
              'venv.Lib.site-packages.IPython.utils.tests', 'venv.Lib.site-packages.IPython.kernel',
              'venv.Lib.site-packages.IPython.testing', 'venv.Lib.site-packages.IPython.testing.tests',
              'venv.Lib.site-packages.IPython.testing.plugin', 'venv.Lib.site-packages.IPython.external',
              'venv.Lib.site-packages.IPython.external.decorators', 'venv.Lib.site-packages.IPython.terminal',
              'venv.Lib.site-packages.IPython.terminal.tests', 'venv.Lib.site-packages.IPython.terminal.pt_inputhooks',
              'venv.Lib.site-packages.IPython.sphinxext', 'venv.Lib.site-packages.IPython.extensions',
              'venv.Lib.site-packages.IPython.extensions.tests', 'venv.Lib.site-packages.tornado',
              'venv.Lib.site-packages.tornado.test', 'venv.Lib.site-packages.tornado.platform',
              'venv.Lib.site-packages.urllib3', 'venv.Lib.site-packages.urllib3.util',
              'venv.Lib.site-packages.urllib3.contrib', 'venv.Lib.site-packages.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.urllib3.packages', 'venv.Lib.site-packages.urllib3.packages.backports',
              'venv.Lib.site-packages.urllib3.packages.ssl_match_hostname', 'venv.Lib.site-packages.wcwidth',
              'venv.Lib.site-packages.wcwidth.tests', 'venv.Lib.site-packages.backcall',
              'venv.Lib.site-packages.colorama', 'venv.Lib.site-packages.dateutil',
              'venv.Lib.site-packages.dateutil.tz', 'venv.Lib.site-packages.dateutil.parser',
              'venv.Lib.site-packages.dateutil.zoneinfo', 'venv.Lib.site-packages.fabulous',
              'venv.Lib.site-packages.fabulous.experimental', 'venv.Lib.site-packages.helowrld',
              'venv.Lib.site-packages.html5lib', 'venv.Lib.site-packages.html5lib._trie',
              'venv.Lib.site-packages.html5lib.filters', 'venv.Lib.site-packages.html5lib.treewalkers',
              'venv.Lib.site-packages.html5lib.treeadapters', 'venv.Lib.site-packages.html5lib.treebuilders',
              'venv.Lib.site-packages.pygments', 'venv.Lib.site-packages.pygments.lexers',
              'venv.Lib.site-packages.pygments.styles', 'venv.Lib.site-packages.pygments.filters',
              'venv.Lib.site-packages.pygments.formatters', 'venv.Lib.site-packages.requests',
              'venv.Lib.site-packages.selenium', 'venv.Lib.site-packages.selenium.common',
              'venv.Lib.site-packages.selenium.webdriver', 'venv.Lib.site-packages.selenium.webdriver.ie',
              'venv.Lib.site-packages.selenium.webdriver.edge', 'venv.Lib.site-packages.selenium.webdriver.opera',
              'venv.Lib.site-packages.selenium.webdriver.chrome', 'venv.Lib.site-packages.selenium.webdriver.common',
              'venv.Lib.site-packages.selenium.webdriver.common.html5',
              'venv.Lib.site-packages.selenium.webdriver.common.actions',
              'venv.Lib.site-packages.selenium.webdriver.remote', 'venv.Lib.site-packages.selenium.webdriver.safari',
              'venv.Lib.site-packages.selenium.webdriver.android', 'venv.Lib.site-packages.selenium.webdriver.firefox',
              'venv.Lib.site-packages.selenium.webdriver.support',
              'venv.Lib.site-packages.selenium.webdriver.phantomjs',
              'venv.Lib.site-packages.selenium.webdriver.webkitgtk',
              'venv.Lib.site-packages.selenium.webdriver.blackberry', 'venv.Lib.site-packages.cookiejar',
              'venv.Lib.site-packages.ipykernel', 'venv.Lib.site-packages.ipykernel.gui',
              'venv.Lib.site-packages.ipykernel.comm', 'venv.Lib.site-packages.ipykernel.pylab',
              'venv.Lib.site-packages.ipykernel.tests', 'venv.Lib.site-packages.ipykernel.inprocess',
              'venv.Lib.site-packages.ipykernel.inprocess.tests', 'venv.Lib.site-packages.pycparser',
              'venv.Lib.site-packages.pycparser.ply', 'venv.Lib.site-packages.traitlets',
              'venv.Lib.site-packages.traitlets.tests', 'venv.Lib.site-packages.traitlets.utils',
              'venv.Lib.site-packages.traitlets.utils.tests', 'venv.Lib.site-packages.traitlets.config',
              'venv.Lib.site-packages.traitlets.config.tests', 'venv.Lib.site-packages.asn1crypto',
              'venv.Lib.site-packages.asn1crypto._perf', 'venv.Lib.site-packages.markupsafe',
              'venv.Lib.site-packages.binaryornot', 'venv.Lib.site-packages.jinja2_time',
              'venv.Lib.site-packages.libfuturize', 'venv.Lib.site-packages.libfuturize.fixes',
              'venv.Lib.site-packages.cookiecutter', 'venv.Lib.site-packages.cryptography',
              'venv.Lib.site-packages.cryptography.x509', 'venv.Lib.site-packages.cryptography.hazmat',
              'venv.Lib.site-packages.cryptography.hazmat.backends',
              'venv.Lib.site-packages.cryptography.hazmat.backends.openssl',
              'venv.Lib.site-packages.cryptography.hazmat.bindings',
              'venv.Lib.site-packages.cryptography.hazmat.bindings.openssl',
              'venv.Lib.site-packages.cryptography.hazmat.primitives',
              'venv.Lib.site-packages.cryptography.hazmat.primitives.kdf',
              'venv.Lib.site-packages.cryptography.hazmat.primitives.ciphers',
              'venv.Lib.site-packages.cryptography.hazmat.primitives.twofactor',
              'venv.Lib.site-packages.cryptography.hazmat.primitives.asymmetric', 'venv.Lib.site-packages.jupyter_core',
              'venv.Lib.site-packages.jupyter_core.tests', 'venv.Lib.site-packages.jupyter_core.utils',
              'venv.Lib.site-packages.webencodings', 'venv.Lib.site-packages.libpasteurize',
              'venv.Lib.site-packages.libpasteurize.fixes', 'venv.Lib.site-packages.jupyter_client',
              'venv.Lib.site-packages.jupyter_client.tests', 'venv.Lib.site-packages.jupyter_client.ioloop',
              'venv.Lib.site-packages.jupyter_client.blocking', 'venv.Lib.site-packages.prompt_toolkit',
              'venv.Lib.site-packages.prompt_toolkit.input', 'venv.Lib.site-packages.prompt_toolkit.layout',
              'venv.Lib.site-packages.prompt_toolkit.lexers', 'venv.Lib.site-packages.prompt_toolkit.output',
              'venv.Lib.site-packages.prompt_toolkit.styles', 'venv.Lib.site-packages.prompt_toolkit.contrib',
              'venv.Lib.site-packages.prompt_toolkit.contrib.telnet',
              'venv.Lib.site-packages.prompt_toolkit.contrib.completers',
              'venv.Lib.site-packages.prompt_toolkit.contrib.regular_languages',
              'venv.Lib.site-packages.prompt_toolkit.filters', 'venv.Lib.site-packages.prompt_toolkit.widgets',
              'venv.Lib.site-packages.prompt_toolkit.clipboard', 'venv.Lib.site-packages.prompt_toolkit.eventloop',
              'venv.Lib.site-packages.prompt_toolkit.shortcuts',
              'venv.Lib.site-packages.prompt_toolkit.shortcuts.progress_bar',
              'venv.Lib.site-packages.prompt_toolkit.completion', 'venv.Lib.site-packages.prompt_toolkit.application',
              'venv.Lib.site-packages.prompt_toolkit.key_binding',
              'venv.Lib.site-packages.prompt_toolkit.key_binding.bindings',
              'venv.Lib.site-packages.prompt_toolkit.formatted_text', 'venv.Lib.site-packages.ipython_genutils',
              'venv.Lib.site-packages.ipython_genutils.tests', 'venv.Lib.site-packages.ipython_genutils.testing',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.idna',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pytoml',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.certifi',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.msgpack',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.util',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.colorama',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.progress',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.requests',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.packaging',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.webencodings',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.req',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.vcs',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.utils',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.models',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.commands',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.operations', 'website_api', 'compare_price',
              '', ''],
    package_dir={'': 'website_api'},
    url='',
    license='',
    author='Akshat Malik',
    author_email='',
    description=''
)
