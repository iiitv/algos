def permute(s):

'''
A recursive funciton to output a list of all the possible permutations of that string.

For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
'''
    out = []
    
    # Base Case
    if len(s) == 1:
        out = [s]
        
    else:
        # For every letter in string
        for i, let in enumerate(s):
            
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):
                
                # Add it to output
                out += [let + perm]

    return out
    
def main():
  permute('abc')

    
if __name__ == '__main__':
    main()
