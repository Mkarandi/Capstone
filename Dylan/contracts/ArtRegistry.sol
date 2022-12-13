pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtRegistry is ERC721Full {
    constructor() public ERC721Full("ArtRegistryToken", "ART") {}

    struct Artwork {
        string name;
        string artist;
        string artJson;
    }

    mapping(uint256 => Artwork) public artCollection;

    event Appraisal(uint256 tokenId, string reportURI, string artJson);
    
    function imageUri(
        uint256 tokenId

    ) public view returns (string memory imageJson){
        return artCollection[tokenId].artJson;
    }


    function registerArtwork(
        address owner,
        string memory name,
        string memory artist,
        string memory tokenURI,
        string memory tokenJSON
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        artCollection[tokenId] = Artwork(name, artist, tokenJSON);

        return tokenId;
    }
