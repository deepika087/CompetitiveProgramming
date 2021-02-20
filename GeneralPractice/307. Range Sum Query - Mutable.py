__author__ = 'deepika'



"""
This is abery buggy approach. Better way to make blocks of array`


private int[] b;
private int len;
private int[] nums;

public NumArray(int[] nums) {
    this.nums = nums;
    double l = Math.sqrt(nums.length);
    len = (int) Math.ceil(nums.length/l);
    b = new int [len];
    for (int i = 0; i < nums.length; i++)
        b[i / len] += nums[i];
}

public int sumRange(int i, int j) {
    int sum = 0;
    int startBlock = i / len;
    int endBlock = j / len;
    if (startBlock == endBlock) {
        for (int k = i; k <= j; k++)
            sum += nums[k];
    } else {
        for (int k = i; k <= (startBlock + 1) * len - 1; k++)
            sum += nums[k];
        for (int k = startBlock + 1; k <= endBlock - 1; k++)
            sum += b[k];
        for (int k = endBlock * len; k <= j; k++)
            sum += nums[k];
    }
    return sum;
}

public void update(int i, int val) {
    int b_l = i / len;
    b[b_l] = b[b_l] - nums[i] + val;
    nums[i] = val;
}
// Accepted

"""
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefix = [self.nums[i] for i in range(len(self.nums))]

        for i in range(1, len(self.nums)):
            self.prefix[i] += self.prefix[i-1]
        print(self.prefix)
        self.cache = {}


    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.cache[index] = val - self.nums[index]


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        effective_sum = 0
        if left == 0:
            effective_sum = self.prefix[right]
        else:
            effective_sum = self.prefix[right] - self.prefix[left - 1]
        #print("effective_sum", effective_sum)
        for i in range(left, right + 1):
            if i in self.cache:
                if right == i:
                    effective_sum += (self.cache[i])
                else:
                    effective_sum += (self.cache[i])* (right - i)
        return effective_sum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
numArray = NumArray([1, 3, 5]);
print(numArray.sumRange(0, 2)); # return 9 = sum([1,3,5])
numArray.update(2, 11);   # nums = [1,2,5]
print(numArray.sumRange(2, 2)); # return 8 = sum([1,2,5])

numArray = NumArray([-1]);
print(numArray.sumRange(0, 0)); # return 9 = sum([1,3,5])
numArray.update(0, 1);   # nums = [1,2,5]
print(numArray.sumRange(0, 0)); # return 8 = sum([1,2,5])
