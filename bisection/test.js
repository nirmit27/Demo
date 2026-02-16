// Generating HASH

import crypto from "crypto";

const hash = crypto.createHash("sha256").update("hello_friend").digest("hex");
console.log(hash);
