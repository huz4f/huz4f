---
date: 2024-02-12
title: "Blockchain & Smart Contracts"
tags: ["Blockchain","Solidity","Swift","Web3"]
author: "Huzaif"
showreadingtime: false
hideSummary: true
draft: false
---

- [Blocks and Hashing](#understanding-code)
- [Smart Contract](#smart-contract)

# Blockchain:

>->  Have written about [Blockchain](https://huz4f.online/articles/blockchain/) in Articles.
>
**Demonstration: How BlockChain works using cocoa and SHA-1 checksum utility**

-> One block connected to the genesis block and hash function with 2 zeroes at start
{{<youtube dsYQxNIGCRk>}} 


>Have also uploaded this swift code on GitHub:  [Here](https://github.com/huz4f/Blockchain) ( needs shasum file for the hash ) 

---

###  Understanding Code:
>Block in a blockchain consists of **Block Header & Body**
>
**The head consists of**:
- Previous block's hash
- Merkel root (compact hash sum of all transactions)
- Block version
- Nonce (it is calculated)
- Timestamp 
- The condition you set for which nonce is calculated

**The body** consists of Transaction lists. Exact contents depend on the type of blockchain. \
Exact compostion can slightly vary from blockchain to blockchain.

Main components of the program for brief understanding of blockchain mechanism:
```swift
class Block : Codable {
    var index: Int = 0
    var previousHash: String = ""
    var hash: String!
    var nonce: Int
    
    private (set) var transactions: [Transaction] = [Transaction]()
    
    var key: String {
        get {
            let transactionsData = try! JSONEncoder().encode(self.transactions)
            let transactionsJSONString = String(data: transactionsData, encoding: .utf8)
            return String(self.index) + self.previousHash + String(self.nonce) + (transactionsJSONString ?? "")
        }
    }
    
    func addTransaction(transaction: Transaction) {
        self.transactions.append(transaction)
    }
    
    init() {
        self.nonce = 0
    }
}
```
This part of the code above is a blueprint.You can clearly see the properties declared in above class. \
Used a read only key for using cryptographic hash of the block \
Key is created by combining the index, previous hash and transaction + finding the right nounce that follows rule we set. In this code i will set it to two initial 0's (Proof of work)
**addTransaction method** adds a transcation to the list \
-used JSON for enabeling transmission

```swift
    class Blockchain : Codable {
    private (set) var blocks: [Block] = [Block]()
    private (set) var smartContracts :[hu] = [TransactionTypeSmartContract()]
    
    
    
    
    init(GenesisBlock: Block) {
        addBlock(GenesisBlock)
    }
    private enum CodingKeys : CodingKey{
        case blocks
    }
    
    func addBlock(_ block: Block) {
        if self.blocks.isEmpty {
            block.previousHash = "0000000000000b0"
            block.hash = generateHash(for: block)
        }
        self.blocks.append(block)
    }
    func getNextBlock(transactions: [Transaction]) -> Block {
        let block = Block()
        transactions.forEach { transaction in
            block.addTransaction(transaction: transaction)
        }

        let previousBlock = getPreviousBlock()
        block.index = self.blocks.count
        block.previousHash = previousBlock.hash
        block.hash = generateHash(for: block)

        return block
    }

    private func getPreviousBlock() -> Block {
        guard let lastBlock = self.blocks.last else {
            // Handle the case when there are no previous blocks
            // For example, you can return a genesis block here
            fatalError("No previous blocks available.")
        }
        return lastBlock
    }
```
This class is container and a manager for instances of block class, managing index and previous hash of new blocks. Creating the chain structure, starting with genesis block.

GenerateHash is initalized (more below)


```swift
    func generateHash(for block: Block) -> String {
        var hash = block.key.sha1Hash()
        
        //proof of work
        while(!hash.hasPrefix("00")){
            block.nonce += 1
            hash = block.key.sha1Hash()
        }
        return hash
    }
}
extension String{

    func sha1Hash() -> String{using shasum}}
```
This is our generateHash function

i have used a loop to find hash with respect to above key defined, \
that follows rule of having intially two zeroes \
SHA-1 func is used here while bitcoin uses SHA-256 and it's first 13 digits are 0 iirc \
using generateHash each block gets it's own unique identfier

---

# Smart Contract:
 **-> Solidity contract for inheritance of assets after death:**


![](/Projects/sol.png)

> Use Truffle and Ganache for simulating local environment, older versions of solidity compiler and node are required (wasted most of my time on this dependecy hell)









