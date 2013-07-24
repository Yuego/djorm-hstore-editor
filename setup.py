from setuptools import setup, find_packages

from hstore_editor.version import __version__

description="""
djorm-ext-hstore extension
"""



setup(
    name="djorm-hstore-editor",
    version=__version__,
    url='https://github.com/Yuego/djorm-hstore-editor',
    license='MIT',
    platforms=['OS Independent'],
    description=description.strip(),
    author='Artem Vlasov',
    author_email='root@proscript.ru',
    maintainer='Artem Vlasov',
    maintainer_email='root@proscript.ru',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'djorm-ext-hstore > 0.4.3',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
    ]
)
