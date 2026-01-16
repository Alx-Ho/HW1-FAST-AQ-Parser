# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # Test reading a valid fasta file
    parser = FastaParser("data/test.fa")
    records = list(parser) # get all records from parser generator
    
    # Check that we got records
    assert len(records) > 0

    # Check that each record is a tuple of (header, sequence)
    first_record = records[0]
    assert len(first_record) == 2
    assert first_record[0] == "seq0"
    
    # Test with bad.fa (missing sequences)
    with pytest.raises(ValueError):
        parser = FastaParser("tests/bad.fa")
        list(parser)
    
    # Test with blank.fa (empty file)
    with pytest.raises(ValueError):
        parser = FastaParser("tests/blank.fa")
        list(parser)


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # Reading a fastq file with FastaParser should give None for seq_name
    parser = FastaParser("data/test.fq")
    records = list(parser)
    first_record = records[0]
    assert first_record[0] is None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # Test reading a valid fastq file
    parser = FastqParser("data/test.fq")
    records = list(parser)
    
    # Check that we got records
    assert len(records) > 0
    
    # Check that each record is a tuple of (header, sequence, quality)
    first_record = records[0]
    assert len(first_record) == 3
    assert first_record[0] == "seq0"

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Reading a fasta file with FastqParser should give None for seq_name
    parser = FastqParser("data/test.fa")
    records = list(parser)
    first_record = records[0]
    assert first_record[0] is None