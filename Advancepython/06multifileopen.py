with (
    open('file1.txt', 'r') as f1,
    open('file2.txt', 'r') as f2
):
    # Process files
    data1 = f1.read()
    data2 = f2.read()
    print("File 1 Content:", data1)
    print("File 2 Content:", data2)
