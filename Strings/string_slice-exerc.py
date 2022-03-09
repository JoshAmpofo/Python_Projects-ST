"""This exercise uses find and slicing to locate the string after colon and convert it to floating point"""
string = 'X-DSPAM-Confidence:0.8475'

print(len(string))

decimal = string.find('0.8475')
print(decimal)

float_str = string[decimal:]
print(float_str)
print(type(float_str))

float_num = float(float_str)
print(float_num)
print(type(float_num))
