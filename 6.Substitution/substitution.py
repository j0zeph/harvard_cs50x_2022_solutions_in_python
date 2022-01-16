import substitution_class as substitution
import substitution_utils as sub_utils


def main():
    sub_utils.print_any_argv_warnings()
    plaintext = input("Plaintext: ")
    sub = substitution.Substitution()
    sub.set_plaintext(plaintext)
    sub.set_key(sub_utils.get_key())
    print("Ciphertext: {}".format(sub.get_ciphertext()))


if __name__ == "__main__":
    main()
