def isPalindrome(x):
    ##判断输入值是否小于0，如果小于0，则返回False（不是回文）
    if x < 0:
        return False

    
    r = 1  ##创建临时变量，作为运算判断的辅助
    ##将r设置与输入值同位的除数（输入为123，则r=100）
    while x / r >= 10:
        r *= 10

    while r > 1:
        left, x =divmod(x, r) ##取得x的第一位数字给left，再去除x的第一位数字
        x, right = divmod(x, 10) ##取得x的最后一位数字给right，再去除x的最后一位数字
        if left != right:
            return False ##头尾相对应的数字不同则返回错误
        r //= 100 ##由于x缩小两位，临时输出也缩小两位

    return True ##头尾相对应的数字全部相同，返回True

##测试方法：
isPalindrome(11)
isPalindrome(-11)
isPalindrome(5)
isPalindrome(5151)
