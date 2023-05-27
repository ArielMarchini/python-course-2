import string


class UsernameContainsIllegalCharacter(Exception):
    """Exception raised when the username contains an illegal character."""

    def __init__(self, char, i):
        self._char = char
        self._index = i

    def __str__(self):
        return 'The username contains an illegal character "{}" at index {}'.format(self._char, self._index)


class UsernameTooShort(Exception):
    """Exception raised when the username is too short."""

    def __str__(self):
        return "The username is too short, you need to have a minimum of 3 characters."


class UsernameTooLong(Exception):
    """Exception raised when the username is too long."""

    def __str__(self):
        return "The username is too long, you need to have a maximum of 16 characters."


class PasswordMissingCharacter(Exception):
    """Exception raised when the password is missing a required character."""

    def __str__(self):
        return "The password is missing a character."


class MissingUppercase(PasswordMissingCharacter):
    """Exception raised when the password is missing an uppercase letter."""

    def __str__(self):
        return super().__str__() + " (Uppercase)"


class MissingLowercase(PasswordMissingCharacter):
    """Exception raised when the password is missing a lowercase letter."""

    def __str__(self):
        return super().__str__() + " (Lowercase)"


class MissingDigit(PasswordMissingCharacter):
    """Exception raised when the password is missing a digit."""

    def __str__(self):
        return super().__str__() + " (Digit)"


class MissingSpecial(PasswordMissingCharacter):
    """Exception raised when the password is missing a special character."""

    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    """Exception raised when the password is too short."""

    def __str__(self):
        return "The password is too short."


class PasswordTooLong(Exception):
    """Exception raised when the password is too long."""

    def __str__(self):
        return "The password is too long."


def check_input(username, password):
    """Check the username and password for validity.

    Args:
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        None

    Raises:
        UsernameContainsIllegalCharacter: If the username contains an illegal character.
        UsernameTooShort: If the username is too short.
        UsernameTooLong: If the username is too long.
        PasswordMissingCharacter: If the password is missing a required character.
        PasswordTooShort: If the password is too short.
        PasswordTooLong: If the password is too long.
    """
    try:
        if len(username) < 3:
            raise UsernameTooShort
        elif len(username) > 16:
            raise UsernameTooLong
        check = True
        for char in username:
            c = char
            i = username.index(c)
            if char not in (string.ascii_letters + string.digits + '_'):
                check = False
                break
        if not check:
            raise UsernameContainsIllegalCharacter(c, i)

        if len(password) < 8:
            raise PasswordTooShort
        elif len(password) > 40:
            raise PasswordTooLong
        if not any(c.isupper() for c in password):
            raise MissingUppercase
        elif not any(c.islower() for c in password):
            raise MissingLowercase
        elif not any(c.isdigit() for c in password):
            raise MissingDigit
        elif not any(c in string.punctuation for c in password):
            raise MissingSpecial

    except UsernameContainsIllegalCharacter as e:
        print(e)
        return False
    except UsernameTooShort as e:
        print(e)
        return False
    except UsernameTooLong as e:
        print(e)
        return False
    except PasswordMissingCharacter as e:
        print(e)
        return False
    except PasswordTooShort as e:
        print(e)
        return False
    except PasswordTooLong as e:
        print(e)
        return False
    else:
        print("OK")
        return True


def main():
    """Main function to get user input for username and password."""
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    exception_raised = check_input(user_name, password)
    while not exception_raised:
        user_name = input("Enter username: ")
        password = input("Enter password: ")
        exception_raised = check_input(user_name, password)


if __name__ == '__main__':
    main()
