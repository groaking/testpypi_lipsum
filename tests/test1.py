# Let's test to import this package from test.pypi.org
# The package should be installed in a separate virtual environment

from testpypi_lipsum import lipsum

if __name__ == "__main__":
    # Print only one sentence
    print('[short_lipsum]')
    print(lipsum.get_short())
    print()
    
    # Print an entire three paragraphs
    print('[long_lipsum]')
    print(lipsum.get_long())
    print()
