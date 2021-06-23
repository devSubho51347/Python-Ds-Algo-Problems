# User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        # self.arr = arr
        # self.n = n
        # self.k = k
        # arr.sort()
        dict1 = {}
        dict2 = {}
        arr = list(set(arr))
        arr.sort()
        diff1 = 1000
        diff2 = 1000
        diff3 = 1000
        diff4 = 1000
        diff5 = 0
        diff = 1000
        print(arr)
        mini = arr[0] + k
        maxi = arr[0] + k
        arr1 = []
        i = 1

        if len(arr) == 1:
            return 0

        for ele in arr:
            if ele - k < 0:
                dict1[ele] = [ele + k, ele + k]
            else:
                dict1[ele] = [ele - k, ele + k]

        arr[0] += k
        print(dict1)

        for ele in arr[1:len(arr):1]:
            print(maxi)
            print()
            print(mini)
            print()

            if dict1[ele][0] < mini:
                diff1 = maxi - dict1[ele][0]
                dict2[diff1] = dict1[ele][0]
                arr1.append(diff1)

            if dict1[ele][0] > maxi:
                diff2 = dict1[ele][0] - mini
                dict2[diff2] = dict1[ele][0]
                arr1.append(diff2)

            if  dict1[ele][0] >= mini and dict1[ele][0] <= maxi:
                diff6 = maxi - dict1[ele][0]
                dict2[diff6] = dict1[ele][0]
                arr1.append(diff6)

            if dict1[ele][1] < mini:
                diff3 = maxi - dict1[ele][1]
                dict2[diff3] = dict1[ele][1]
                arr1.append(diff3)

            if dict1[ele][1] > maxi:
                diff4 = dict1[ele][1] - mini
                dict2[diff4] = dict1[ele][1]
                arr1.append(diff4)

            if dict1[ele][1] >= mini and dict1[ele][1] <= maxi:
                diff7 = maxi - dict1[ele][1]
                dict2[diff7] = dict1[ele][1]
                arr1.append(diff7)

            diff5 = min(arr1)
            print(arr1)
            arr1 = []
            if dict2[diff5] < mini:
                arr[i] = dict2[diff5]

                mini = dict2[diff5]

            elif dict2[diff5] > maxi:

                arr[i] = dict2[diff5]

                maxi = dict2[diff5]

            diff = maxi - mini

            # if diff5 < diff:
            #     diff = diff5
            #     arr[i] = dict2[diff]
            #
            #     if dict2[diff] < mini:
            #
            #         mini = dict2[diff]
            #
            #     elif dict2[diff] > maxi:
            #
            #         maxi = dict2[diff]
            #
            # elif diff5 > diff:
            #
            #     diff = diff5
            #     arr[i] = dict2[diff]
            #
            #     if dict2[diff] < mini:
            #
            #         mini = dict2[diff]
            #
            #     elif dict2[diff] > maxi:
            #
            #         maxi = dict2[diff]

            i = i + 1
            print(dict2)
            dict2 = {}

        return diff


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
