import { exec } from "node:child_process";
import * as fs from "fs";
import path from "path";
import { promisify } from "node:util";

const execPromise = promisify(exec);
const dir = '/home/dumbcoo/orange-alert/dataset/ucllc-raw/';
const outdir = '/home/dumbcoo/orange-alert/experiments_mythril/output/';
const names = fs.readdirSync(dir);
const processesPerRound = 16;

console.log(names);

for (let i = 0; i < names.length; i += processesPerRound) {
    let promises = [];
    console.log(`i=${i}`);

    for (let j = i; j < i + processesPerRound && j < names.length; ++j) {
        console.log('processing ' + names[j]);

        const promise = execPromise(`myth a -f ${path.join(dir, names[j])} --bin-runtime --execution-timeout 1800`)
            .then(({ stdout, stderr }) => {
                if (stderr) {
                    fs.writeFileSync(path.join(outdir, `err_${names[j]}`), stderr);
                }
                fs.writeFileSync(path.join(outdir, `out_${names[j]}`), stdout);
            })
            .catch(err => {
                fs.writeFileSync(path.join(outdir, `err_${names[j]}`), err.stderr);
                fs.writeFileSync(path.join(outdir, `out_${names[j]}`), err.stdout);
            });

        promises.push(promise);
    }

    await Promise.all(promises);
}