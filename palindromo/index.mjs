import readline from "node:readline";
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
rl.question("Introduce una palabra\n", (word) => {
  const fixed = word.replace(/\s/g, "").toLocaleLowerCase();
  const reverse = fixed.replace(/\s/g, "").split("").reverse().join("");
  console.log(`${fixed} y ${reverse}`);
  console.log(reverse === fixed ? "Es palindromo" : "No es palindromo");
  rl.close();
});
