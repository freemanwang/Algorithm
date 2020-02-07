'''
实现一个repeat函数，使一个函数每间隔固定时间执行一次，共执行N次，如
function repeat(fn, interval, n) {
  // TODO
}

repeat(() => console.log('hello'), 3000, 5);
// 每隔3秒打印hello，共打印5次
'''

# 本题要求JS实现，所以去 webstorm 里写了复制过来，下面是 JS 代码

'''
// eslint-disable-next-line no-unused-vars
function repeat (fn, timeDelay, times) {
  let count = 1
  while (count <= times) {
    setTimeout(fn, timeDelay * count * 1000)
    count++
  }
}
// eslint-disable-next-line no-unused-vars
function fn () {
  console.log('hello')
}
repeat(fn, 3, 5)
'''
