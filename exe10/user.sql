/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50709
Source Host           : localhost:3306
Source Database       : test_db

Target Server Type    : MYSQL
Target Server Version : 50709
File Encoding         : 65001

Date: 2020-05-08 09:26:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL COMMENT '主键',
  `name` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '用户姓名',
  `age` int(3) DEFAULT NULL COMMENT '年龄',
  `addtime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录添加时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'Bob', '26', null);
INSERT INTO `user` VALUES ('2', 'Jackie', '25', null);
INSERT INTO `user` VALUES ('3', 'TOM', '21', null);
INSERT INTO `user` VALUES ('4', 'hahah', '19', null);
INSERT INTO `user` VALUES ('5', 'Bob', '20', null);
INSERT INTO `user` VALUES ('7', 'cynthia', '21', null);
INSERT INTO `user` VALUES ('8', 'Marry', '21', '2020-05-08 08:56:21');
INSERT INTO `user` VALUES ('6', 'laowang', '50', '2020-05-08 08:59:56');
INSERT INTO `user` VALUES ('9', 'laoli', '50', '2020-05-08 09:02:31');
