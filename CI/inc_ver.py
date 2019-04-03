'''
Update version (VERSION file in the repository root)
with commit number:
major.minor.commit

The script is only to be used in Travis CI,
see .travis.yml for more details.

The script uses Travis enviroment variables, see
https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
for more details.
'''

import os


def main():
    '''
    if not os.environ.get('TRAVIS', False):
        print(__doc__)
        return 1
    '''

    version = '0.0.0'
    with open('VERSION') as f:
        version = f.read()
    ver = version.split('.')
    commit = os.environ.get('TRAVIS_COMMIT')
    new_ver = f'{ver[0]}.{ver[1]}.{commit}'
    gh_token = os.environ.get('GH_TOKEN')

    with open('VERSION', 'w') as f:
        f.write(new_ver)

    os.system(f'git config --global user.email "travis@travis-ci.org"')
    os.system(f'git config --global user.name "Travis CI"')
    os.system(f'git remote set-url origin https://{gh_token}@github.com/tableau/TabPy > /dev/null 2>&1')
    os.system(f'git add -u')
    os.system(f'git commit -m "[ci skip] increase version to {new_ver}"')
    branch = os.environ.get('TRAVIS_BRANCH')
    os.system(f'git push origin HEAD:{branch}')
    return 0


if __name__ == "__main__":
    main()
