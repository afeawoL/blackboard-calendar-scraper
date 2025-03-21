om setuptools import setup, find_packages

setup(
    name='blackboard_calendar_scraper',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'selenium',
        'google-auth',
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'google-api-python-client',
        'dateparser',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'blackboard_scraper = main:main'
        ]
    },
    author='Your Name',
    description='A script to scrape Blackboard assignments and sync them with Google Calendar.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
