---
date: 2024-02-13
title: "Blockchain & Smart Contracts"
tags: ["Blockchain","Solidity","Swift"]
author: "Me"
showreadingtime: false
hideSummary: true
draft: true
---
# Blockchain:
>-> I have written about [Blockchain](/Articles/BlockChain.md) in Articles.
>
Demonstration of how BlockChain works using cocoa and inbuilt  SHA-1 checksum utility

{{<youtube dsYQxNIGCRk>}} 
#### -> Shows one block connected to the genesis block and hash function with 2 zeroes at start

Have also uploaded this swift code on GitHub:  [Here](https://github.com/huz4f/Blockchain) ( needs shasum file for the hash ) 
###  Understanding Code:
Here are main components of this program for understanding blockchain mechanism
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



# Smart Contract:
 **-> Solidity contract for inheritance of assets after death:**


![](/images/sol.png)

> Use Truffle and Ganache for simulating local environment, older versions of solidity compiler and node are required (wasted most of my time on this dependecy hell)









