# ABC-XML Converter

## Overview

This repository provides two main functions for converting between ABC and XML (MusicXML) formats:

- `convert_abc2xml`: Converts ABC files to XML format.
- `convert_xml2abc`: Converts XML (MusicXML) files to ABC format.

These functions are heavily built on the `abc2xml` and `xml2abc` utilities developed by Willem G. Vree and contributors.

- **abc2xml**: A command-line utility that translates ABC notation into MusicXML.
- **xml2abc**: A command-line utility that translates MusicXML into ABC+ notation.

The original tools were designed for use via a command-line interface (CLI). The goal of this project was to create a Python package that allows users to convert files from ABC to XML and vice versa by calling the conversion functions directly, without needing to use the CLI. This makes the conversion process easier to integrate into other Python workflows.

## Installation

## Installation

You can install the package via PyPi:

```sh
pip install abc-xml-converter
```
After installing the package via PyPi, you can simply import the conversion functions:

```
from abc_xml_converter import convert_abc2xml
from abc_xml_converter import convert_xml2abc
```

If you want to contribute to the project, clone the repository:

```
git clone https://github.com/sebastian-eck/abc-xml-converter.git
```

Ensure you have Python installed. This project is compatible with Python 3.

## Usage

You can use these functions in your own scripts or run the provided example script to see how they work.

### Example Usage

Create a file `example_usage.py` with the following content:

```python
from abc_xml_converter import convert_abc2xml
from abc_xml_converter import convert_xml2abc

# Prepare ABC and XML files as strings

def read_abc_file(filename, errmsg='read error: '):
    try:
        if filename == '-.abc':
            import sys
            content = sys.stdin.read()
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
        return content
    except Exception as e:
        print(errmsg + repr(e) + ' ' + filename)
        return None


abc_file_txt = read_abc_file("files/abc/Bach 1.abc", errmsg='read error: ')

def read_xml_file(filename, errmsg='read error: '):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        print(errmsg + repr(e) + ' ' + filename)
        return None

xml_file_txt = read_xml_file("files/xml_files/Bach 2.xml", errmsg='read error: ')


def main():

    # 1) Example usage of convert_abc2xml


    # a) Converting ABC to XML and returning as string

    print("Converting ABC to XML and returning as string:")

    xml_content = convert_abc2xml(file_to_convert="files/abc/Bach 1.abc")
    print(xml_content)

    # b) Converting ABC to XML and saving to directory

    convert_abc2xml(file_to_convert="files/abc/Bach 1.abc", output_directory="files/xml_converted")

    # c) Converting ABC string to XML and returning as string

    print("Converting ABC string to XML and returning as string:")

    xml_content = convert_abc2xml(file_to_convert=abc_file_txt, file_to_convert_is_txt=True)
    print(xml_content)

    # d) Converting ABC string to XML and saving to directory:")

    convert_abc2xml(file_to_convert=abc_file_txt, output_directory="files/xml_converted", file_to_convert_is_txt=True)


    # 2) Example usage of convert_xml2abc


    # a) Converting XML to ABC and returning as string

    print("\nConverting XML to ABC and returning as string:\n")

    abc_content = convert_xml2abc(file_to_convert="files/xml_files/Bach 2.xml")
    print(abc_content)

    # b) Converting XML to ABC and saving to directory

    convert_xml2abc(file_to_convert="files/xml_files/Bach 2.xml", output_directory="files/abc_converted")

    # c) Converting XML string to ABC and returning as string

    print("\nConverting XML string to ABC and returning as string:\n")

    abc_content = convert_xml2abc(file_to_convert=xml_file_txt, file_to_convert_is_txt=True)
    print(abc_content)

    # d) Converting XML string to ABC and saving to directory

    convert_xml2abc(file_to_convert=xml_file_txt, output_directory="files/abc_converted", file_to_convert_is_txt=True)


if __name__ == "__main__":
    main()
```

Run the example script:

```sh
python example_usage.py
```

### Function: `convert_abc2xml`

#### Parameters

- `output_directory` (str, optional): Directory to store the resulting XML files. If an empty string, the function will not export the file, but return the XML content as a string. Default is an empty string.
- `file_to_convert` (str, optional): Path to the ABC file to be converted or the content of the ABC file as a string. Default is an empty string.
- `file_to_convert_is_txt` (bool, optional): If True, `file_to_convert` is expected to be a string containing the ABC content. Default is False.
- `skip_tunes` (tuple of int, optional): Tuple containing two integers: the number of tunes to skip and the maximum number of tunes to read. Default is (0, 1).
- `page_format` (str, optional): Page format settings including scale, page height, page width, and margins. Format: 'scale,pageheight,pagewidth,leftmargin,rightmargin,topmargin,botmargin'. Default is an empty string.
- `mxl_mode` (str, optional): Mode to store as compressed MXL (MusicXML), either 'add' (or 'a') to add or 'replace' (or 'r') to replace. Default is an empty string.
- `show_rests` (bool, optional): If True, show whole measure rests in merged staffs. Default is False.
- `use_title_as_filename` (bool, optional): If True, use the tune title as the file name. Default is False.
- `line_break_at_eol` (bool, optional): If True, enable line breaks at the end of lines. Default is False.
- `meta_map` (str, optional): Mapping of info fields to XML metadata. Format: 'field1:tag1,field2:tag2,...'. Default is an empty string.
- `force_string_fret` (bool, optional): If True, force string/fret allocations for tablature staves. Default is False.

#### Returns

- `str` or `None`: The XML content as a string if `output_directory` is an empty string, otherwise `None`.

### Function: `convert_xml2abc`

#### Parameters

- `output_directory` (str, optional): Directory to store the resulting ABC files. If an empty string, the function will not export the file, but return the ABC content as a string. Default is an empty string.
- `file_to_convert` (str, optional): Path to the MusicXML file to be converted or the content of the XML file as a string. Default is an empty string.
- `file_to_convert_is_txt` (bool, optional): If True, `file_to_convert` is expected to be a string containing the XML content. Default is False.
- `unfold_repeats` (bool, optional): If True, unfold simple repeats. Default is False.
- `midi_output_level` (int, optional): MIDI output level: 0 -> no %%MIDI, 1 -> minimal %%MIDI, 2 -> all %%MIDI. Default is 0.
- `credit_text_filter` (int, optional): Set credit text filter level. Default is 0.
- `note_length` (int, optional): Set L:1/D (e.g., default note length). Default is 0.
- `chars_per_line` (int, optional): Max number of characters per line (default 100). Default is 0.
- `bars_per_line` (int, optional): Max number of bars per line. Default is 0.
- `volta_behavior` (int, optional): Volta typesetting behavior. Default is 0.
- `no_line_breaks` (bool, optional): If True, output with no line breaks. Default is False.
- `page_format` (str, optional): Page format (e.g., scale, pageheight, pagewidth, margins). Default is an empty string.
- `js_compatibility` (bool, optional): If True, switch for compatibility with JavaScript version. Default is False.
- `translate_staff` (bool, optional): If True, translate percussion and tablature staff to ABC code with %%map, %%voicemap. Default is False.
- `shift_note_heads` (bool, optional): If True, shift note heads 3 units left in a tablature staff. Default is False.
- `start_stop_first_voice` (bool, optional): If True, start-stop directions always to the first voice of the staff. Default is False.
- `skip_pedal` (bool, optional): If True, skip all pedal directions. Default is True.
- `translate_stems` (bool, optional): If True, translate stem directions. Default is False.
- `read_from_stdin` (bool, optional): If True, read XML file from standard input. Default is False.

#### Returns

- `str` or `None`: The ABC content as a string if `output_directory` is an empty string, otherwise `None`.

## Acknowledgments

This project heavily builds on the following utilities; both files have been edited and adopted to the purpose of this project.

Both original files can be downloaded via the following URLs:

abc2xml: https://wim.vree.org/svgParse/abc2xml.html

xml2abc: https://wim.vree.org/svgParse/xml2abc.html

(last accessed: 27.06.2024)

### abc2xml (Willem G. Vree)

abc2xml is a command-line utility that translates ABC notation into MusicXML.

Most elements from ABC are translated, but some translations are only partially implemented.

The original software was distributed with the following license:

```
Copyright (C) 2012-2018: Willem G. Vree
Contributions: Nils Liberg, Nicolas Froment

, Norman Schmidt, Reinier Maliepaard, Martin Tarenskeen,
               Paul Villiger, Alexander Scheutzow, Herbert Schneider, David Randolph, Michael Strasser

This program is free software; you can redistribute it and/or modify it under the terms of the
Lesser GNU General Public License as published by the Free Software Foundation;

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the Lesser GNU General Public License for more details. <http://www.gnu.org/licenses/lgpl.html>.
```

### xml2abc (Willem G. Vree)

xml2abc is a command-line utility that translates MusicXML into ABC+ notation. Parts of MusicXML that lie beyond the scope of the ABC standard 2.1 are not translated. For example, specific positioning information and slurs spanning staves.

All non-standard extensions of ABC supported by abc2xml are also supported by xml2abc. For instance, tablature and percussion scores can be translated from MusicXML into ABC and back to MusicXML without significant loss of information.

The original software was distributed with the following license:

```
Copyright (C) 2012-2018: Willem G. Vree
Contributions: Nils Liberg, Nicolas Froment, Norman Schmidt, Reinier Maliepaard, Martin Tarenskeen,
               Paul Villiger, Alexander Scheutzow, Herbert Schneider, David Randolph, Michael Strasser

This program is free software; you can redistribute it and/or modify it under the terms of the
Lesser GNU General Public License as published by the Free Software Foundation;

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the Lesser GNU General Public License for more details. <http://www.gnu.org/licenses/lgpl.html>.
```

### pyparsing.py (not edited)

The original software was distributed with the following license:

```
# Copyright (c) 2003-2013  Paul T. McGuire
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
```

## Contributing

Feel free to fork this repository, make your changes, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the GNU Lesser General Public License. See the [LICENSE](LICENSE) file for details.
```