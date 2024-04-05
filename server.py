def calculate_bucket_id(file_size):

    digit_sum = 0
    while file_size > 0:
        digit_sum += file_size % 10
        file_size//= 10
    return digit_sum

def bucket_id(num_files, file_sizes):

    lis = []
    for i in file_sizes:
        lis = calculate_bucket_id(i)
        lis.append(bucket_id)
    return lis

num_files = int(input("Enter the number of files: "))
file_sizes = list(map(int, input("Enter the file sizes separated by space: ").split()))


lis = bucket_id(num_files, file_sizes)
print(" ".join(map(str, lis)))
