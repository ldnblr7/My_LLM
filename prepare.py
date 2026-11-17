import sys


def main():
    if len(sys.argv) < 4:
        print("Commandline requires three arguments: input, output, sample size.")
        exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sample_size = sys.argv[3]
    with open(input_file) as f:
        text = f.read()
    sample = text[:int(sample_size)]
    character_to_id = encode_dictionary(sample)
    id_to_character = decode_dictionary(character_to_id)
    data = encode(sample, character_to_id)
    split_index = int(round(len(data) * 0.9, 0))
    training_data = data[:split_index]
    validation_data = data[split_index:]
    printer(decode(training_data, id_to_character), output_file)

def encode_dictionary(text):
    """
    Returns dictionary
    key: character
    value: number
    """
    character_to_id = {}
    count = 0
    for character in text:
        if not character in character_to_id.keys():
            character_to_id[character] = count
            count += 1
    return character_to_id

def decode_dictionary(dictionary):
    """
    Returns dictionary
    key: Number
    value: Character
    """
    id_to_character = {}
    for key in dictionary.keys():
        id_to_character[dictionary[key]] = key
    return id_to_character


def encode(text, character_to_id):
    """
    :param text: Input text file.
    :param dictionary:
    :return:
    """
    tokens_id = []
    for character in text:
        tokens_id.append(character_to_id[character])
    return tokens_id


def decode(encoded, id_to_character):
    """

    :param encoded: A tokenized text file
    :param id_to_character: Dictionary from Decoded function.
    :return: encoded de-tokenized into normal text.
    """
    decoded = ""
    for character in encoded:
        decoded += id_to_character[character]
    return decoded


def printer(decoded, output_file):
    """
    Outputs decoded into output_file
    :param decoded: A decoded input file
    :param output_file: An output file.
    :return: void
    """
    output = ""
    for character in decoded:
        output += character
    output += "\n"
    with open(output_file, 'a') as file:
        file.write(output)


if __name__ == '__main__':
    main()
