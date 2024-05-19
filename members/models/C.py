# !pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# pip install -U git+https://github.com/PrithivirajDamodaran/Gramformer.git

from gramformer import Gramformer
import torch

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1212)

gf = Gramformer(models = 1, use_gpu=False)

# Assuming gf is some grammar correction library that has the correct and highlight methods
# from gramformer import Gramformer
# import torch33
# def set_seed(seed):
#   torch.manual_seed(seed)
#   if torch.cuda.is_available():
#     torch.cuda.manual_seed_all(seed)

# set_seed(1212)


gf = Gramformer(models = 1, use_gpu=False)
wrong_grammar = "I is working not now, tomorrow we don't know to do"


def to_correct_word(word):
  need_to_correct_word = word

  corrected_sentence = gf.correct(need_to_correct_word)

  if isinstance(corrected_sentence, set):
    corrected_sentence = ' '.join(corrected_sentence)

  # highlighted_output = gf.highlight(need_to_correct_word, corrected_sentence)

  return corrected_sentence

def to_show_highlight(wrong_word, correct_word):

  highlighted_output = gf.highlight(wrong_word, correct_word)

  return highlighted_output

store_correct = to_correct_word(wrong_grammar)

print("Correct: ", store_correct)

highlight_word = to_show_highlight(wrong_grammar, store_correct)

print("Highlighted: ", highlight_word)


# import difflib

# # Function to highlight differences
# def highlight_differences(wrong, correct):
#     diff = difflib.ndiff(wrong.split(), correct.split())
#     return ' '.join([f"**{word[2:]}**" if word.startswith('+ ') else word[2:] for word in diff if not word.startswith('- ')])

# # Input with wrong grammar
# wrong_grammar = "I is working not now, tomorrow we don't know to do. Radom peple is not trying to please all, I dnot what to do, bcuz i am not trying"

# # Assuming gf is the grammar correction object with a correct method
# corrected_sentence = gf.correct(wrong_grammar)

# # Debugging: Check the types of the variables
# print(f"Type of wrong_grammar: {type(wrong_grammar)}")  # Should be <class 'str'>
# print(f"Type of corrected_sentence: {type(corrected_sentence)}")  # Should be <class 'str'>

# # Ensure the corrected_sentence is a string
# if isinstance(corrected_sentence, set):
#     corrected_sentence = ' '.join(corrected_sentence)

# # Highlight the differences
# highlighted_output = gf.highlight(wrong_grammar, corrected_sentence)

# Print the highlighted output
# print(highlighted_output)
# print(corrected_sentence)


# influent_sentences = [
#     "He are moving here.",
#     "the collection of letters was original used by the ancient Romans",
#     "We enjoys horror movies",
#     "Anna and Mike is going skiing",
#     "I will eat fish for dinner and drank milk",
#     "what be the reason for everyone leave the comapny"
# ]

# for influent_sentence in influent_sentences:
#     corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
#     print(f"Type of corrected_sentences: {type(corrected_sentences)}")
#     print("[Input] ", influent_sentence)
#     for corrected_sentence in corrected_sentences:
#       print(f"Type of corrected_sentences: {type(corrected_sentence)}")
#       print("[Edits] ", gf.highlight(influent_sentence, corrected_sentence))
#     print("-" *100)
