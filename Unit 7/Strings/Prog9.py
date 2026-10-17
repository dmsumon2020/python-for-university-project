# বিল্ট-ইন স্ট্রিং অপারেশনসমূহের উদাহরণ
sample_string = "Python is a good prog., Python is easy to learn, Python is easy to understand."

# ১. নির্দিষ্ট শব্দ কতবার আছে তা গণনা করা
count_val = sample_string.count("Python")
print("Count: ", count_val)

# ২. সব অক্ষর ছোট হাতের কি না তা পরীক্ষা করা
lower_check = sample_string.islower()
print("lower_check: ", lower_check)

# ৩. স্ট্রিংকে ভেঙে শব্দের লিস্টে রূপান্তর করা
split_words = sample_string.split()
print("split_words: ", split_words)

# ৪. স্ট্রিং নির্দিষ্ট অক্ষর দিয়ে শেষ হয় কি না দেখা
ends_check = sample_string.endswith(".")
print("ends_check: ", ends_check)

# ৫. নির্দিষ্ট প্রস্থে টেক্সট সেন্টার করা
center_text = sample_string.center(10)
print("center_text: ", center_text)

# ৬. সব অক্ষর আলফানিউমেরিক কি না যাচাই করা
alnum_check = sample_string.isalnum()
print(alnum_check)

# ৭. সব অক্ষর সংখ্যাসূচক কি না পরীক্ষা করা
numeric_check = sample_string.isnumeric()
print(numeric_check)

# ৮. প্রতিটি শব্দের প্রথম অক্ষর ক্যাপিটাল করা
title_text = sample_string.title()
print(title_text)