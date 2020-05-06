create database if not exists ProductFinder;
use ProductFinder;

CREATE TABLE `ProductFinder`.`product` (
    `itemNumber` INT(255) NOT NULL , 
    `productPrice` DOUBLE NOT NULL , 
    `productName` VARCHAR(500) NOT NULL , 
    `productLink` VARCHAR(500) NOT NULL , 
    `productDiscount` INT(10) NOT NULL ,
    `productDiscoverDate` VARCHAR(50) NOT NULL ,
    `store_idstore` INT NOT NULL ,
    `productImg` VARCHAR(500) NOT NULL )
ENGINE = InnoDB;