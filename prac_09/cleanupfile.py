"""
CP1404/ Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {:<45} to {:<45}".format(filename, new_name))

        # Rename file to new name - in place
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")

    """ This only replaces it for name with a space
    for eg,  "This is Practical 9.txt"   goes to      "This_is_Practical_9.txt"
    eg,      "ThisIsPractical9.txt"       goes to      "ThisIsPractical9.txt"
    """
    return new_name


main()