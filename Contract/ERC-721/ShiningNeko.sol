pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";


contract ShiningNeko is ERC721, Ownable {
    using Counters for Counters.Counter;
    string public fileExtention = ".json";
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("ShiningNeko", "SNEKO") {}

    function _baseURI() internal pure override returns (string memory) {
        return "https://shiningneko.metatory.co.kr/json/";
    }

    function safeMint(address to) public onlyOwner {
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);
    }

      function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 ? string(abi.encodePacked(baseURI, tokenId.toString(), fileExtention)) : "";
    }

    function batchMint(address to, uint amount) public onlyOwner{
        for (uint i = 0; i < amount; i++) {
            safeMint(to);
        }
    }
	function withdraw() public payable onlyOwner {
        (bool success, ) = payable(msg.sender).call{value: address(this).balance}("");
        require(success);
    }
}