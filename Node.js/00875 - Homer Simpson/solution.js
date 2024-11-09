const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (numbers) => {

  var num = numbers.split(' ');
  var M = parseInt(num[0]);
  var N = parseInt(num[1]);
  var T = parseInt(num[2]);

  //console.log("M = %d; N = %d; T = %d;", M, N, T);
  var results = [];
  var times = [];
  var i = 0;

  if (N > M) {
    var temp = N;
    N = M;
    M = temp;
  }

  while (T > 0)
  {
    results.push(parseInt(T / N) + i);
    times.push(T % N);
    if (T % N == 0 || i > 50)
      break;
    T -= M;
    i++;
  }

  var minTimes = Math.min.apply(null, times);

  if (minTimes == 0)
    console.log(results[times.indexOf(minTimes)]);
  else
    console.log(results[times.indexOf(minTimes)], minTimes);

  rl.close();
});
