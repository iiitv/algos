
def permute_my_string(str):
    output_string = []
    '''
        This is a recursive solution to the string permutation problem.
        The user is supposed to return all the permutations for a given string.
    '''
    # Base Case
    if len(str) == 1:
        output_string = [str]
    else:
        # For every letter in String
        for i, letter in enumerate(str):
            # for every permutation resulting from Step 2 and 3 described above
            for perm in permute_my_string(str[:i] + str[i+1:]):
                # Add it to output
                output_string += [letter + perm]
    return output_string


def main():
    print(permute_my_string("abc"))


if __name__ == '__main__':
    main()
