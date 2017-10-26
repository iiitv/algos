def permute_string(my_str):
    string_list = []
    # This is a recursive solution to the string permutation problem.
    # The user is supposed to return all the permutations for a given string.
    # Base Case
    if len(my_str) == 1:
        string_list = [my_str]
    else:
        # For every letter in String
        for i, letter in enumerate(my_str):
            # for every permutation resulting from Step 2 and 3 described above
            for perm in permute_string(my_str[:i] + my_str[i+1:]):
                # Add it to output
                string_list += [letter + perm]
    return string_list


def main():
    print(permute_string("abc"))


if __name__ == '__main__':
    main()
