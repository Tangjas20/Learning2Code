from little_battle import load_config_file
import sys

# Don't remove any comments in this file

# Please create appropriate invalid files in the folder "invalid_files"
# for each unit test according to the comments below and
# then complete them according to the function name
#
def test_file_not_found():
    # no need to create a file for FileNotFound
  try:
    load_config_file("randomfilename")
  except FileNotFoundError as e:
      assert str(e) == "", "error message incorrect"
  except Exception as e:
      assert False, "wrong error type"


def test_format_error():
      folder_path = "./invalid_files/"
      try:
        load_config_file(folder_path + "format_error.txt")
      except SyntaxError as e:
        assert str(e) == "Invalid Configuration File: format error!", "error message incorrect"
      except Exception as e:
        assert False, "wrong error type"


def test_frame_format_error():
   #add "frame_format_error_file.txt" in "invalid_files"
      folder_path = "./invalid_files/"
      try:
        load_config_file(folder_path + "frame_format_error.txt")
      except SyntaxError as e:
        assert str(e) == "Invalid Configuration File: frame should be in format widthxheight", "error message incorrect"
      except Exception as e:
        assert False, "wrong error type"

def test_frame_out_of_range():
  # add "format_out_of_range_file.txt" in "invalid_files"
    folder_path = "./invalid_files/"
    try:
        load_config_file(folder_path + "frame_out_of_range.txt")
    except ArithmeticError as e:
        assert str(e) == "Invalid Configuration File: width and height should range from 5 to 7!", "error message incorrect"
    except Exception as e:
        assert False, "wrong error type"

def test_non_integer():
   # add "non_integer_file.txt" in "invalid_files"
    folder_path = "./invalid_files/"
    try:
        load_config_file(folder_path + "non_integer.txt")
    except ValueError as e:
        assert str(e) == "Invalid Configuration File: Water contains non integer characters", "error message incorrect"
    except Exception as e:
        assert False, "wrong error type"

def test_out_of_map():
  # add "out_of_map_file.txt" in "invalid_files"
    folder_path = "./invalid_files/"
    try:
        load_config_file(folder_path + "out_of_map_file.txt")
    except ArithmeticError as e:
        assert str(e) == "Invalid Configuration File: Water contains a position that is out of map", "error message incorrect"
    except Exception as e:
        assert False, "wrong error type"

def test_occupy_home_or_next_to_home():
  # add two invalid files: "occupy_home_file.txt" and
  # "occupy_next_to_home_file.txt" in "invalid_files"
    folder_path = "./invalid_files/"
    try:
        load_config_file(folder_path + "occupy_home_file.txt")
        load_config_file(folder_path + "occupy_next_to_home.txt")
    except ValueError as e:
        assert str(e) == "Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied", "error message incorrect"
    except Exception as e:
        assert False, "wrong error type"
      
 # def test_duplicate_position():
  # add two files: "dupli_pos_in_single_line.txt" and
  # "dupli_pos_in_multiple_lines.txt" in "invalid_files"
  #  pass

def test_odd_length():
  # add "odd_length_file.txt" in "invalid_files"
    folder_path = "./invalid_files/"
    try:
        load_config_file(folder_path + "odd_length.txt")
    except SyntaxError as e:
        assert str(e) == "Invalid Configuration File: Water has an odd number of elements!", "error message incorrect"
    except Exception as e:
        assert False, "wrong error type"

def test_valid_file():
  # no need to create file for this one, just test loading config.txt
    try:
      assert load_config_file('config.txt') == ([('0', '0'), ('4', '2'), ('1', '3')], [('0', '2'), ('2', '4')], [('0', '4'), ('3', '1')], [('4', '1'), ('2', '2')]), "values are wrong"
    except:
      print("testing has failed")

      

 #you can run this test file to check tests and load_config_file
if __name__ == "__main__":
  test_file_not_found()
  test_format_error()
  test_frame_format_error()
  test_frame_out_of_range()
  test_non_integer()
  test_out_of_map()
  test_occupy_home_or_next_to_home()
  #test_duplicate_position()
  test_odd_length()
  test_valid_file()