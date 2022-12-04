integer, parameter :: n = 3
integer, parameter :: m = 3
integer, parameter :: k = 3
character(len=1), parameter :: str1 = "ABC"
character(len=1), parameter :: str2 = "XYZ"
integer, parameter :: arr(n,m,k) = reshape([3,4,8,1,5,9,2,6,7],shape(arr))
character(len=*) :: fname
character(len=1) :: c1, c2
integer :: nlines, i, j, k, res, a
open(1, file="inp.txt", status="old")
read(1, *, iostat=nlines)
close(1)
open(2, file="out.txt", status="unknown")
do i = 1, nlines
    read(1, *, iostat=a)
    j = index(str1, c1)
    k = index(str2, c2)
    res = res + arr(j,k)
enddo
write(2, *) res
close(2)