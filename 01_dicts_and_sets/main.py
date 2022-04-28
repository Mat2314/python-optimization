"""Module contains functions testing dicts and sets performance"""

# Make sure to add parent directory to the path
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from dis import dis
from utils.custom_decorators import separate_function, measure_time

@separate_function
def keyword_or_characters():
    """Check which declaration of dict and set is better:
    set() vs {}
    dict() vs {}
    """
    
    # Test set declaration 
    print("Declaring set with set() keyword")
    print(dis('set([1])'))
    
    print(50*'-')
    print("Declaring set with {} characters")
    print(dis('{1}'))
    
    print(50*'-')
    print("Declaring dict with dict() keyword")
    print(dis('dict([("key","value")])'))
    
    print(50*'-')
    print("Declaring dict with {} characters")
    print(dis('{[("key","value")]}'))


if __name__ == '__main__':
    keyword_or_characters()