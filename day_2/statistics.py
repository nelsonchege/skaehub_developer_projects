# create a list
main_list = [2, 3, 34, 4, 94, 4, 27, 7, 89, 9, 9, 74]

print(main_list)
# the statistics to be done are
# Mean,Median
# mean
# for mean is the sum divided to the length of the list
mean = sum(main_list) / len(main_list)
print("the mean is:"+str(mean))


# median
# define a function that will hold the medium function
def median(nums):
    # first sort the list
    nums.sort()
    # if statement will be used to chake if the list can be split into half
    if len(nums) % 2 == 0:
        # when it can split the number then pick hte middle two and gives the avarage
        return int(nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
    else:
        # when it can not be split the number then pick the middle one
        return nums[len(nums) // 2]


print("the median for is:"+str(median(main_list)))




