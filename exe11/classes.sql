/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : class

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 25/06/2020 04:51:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for classes
-- ----------------------------
DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes`  (
  `name` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `time` time(0) NOT NULL,
  `is_selected` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classes
-- ----------------------------
INSERT INTO `classes` VALUES ('计算机组成结构', '星期二', '08:00:00', '否');
INSERT INTO `classes` VALUES ('数据库原理', '星期一', '08:00:00', '否');
INSERT INTO `classes` VALUES ('软件工程', '星期二', '10:10:00', '否');
INSERT INTO `classes` VALUES ('编译技术', '星期三', '14:00:00', '否');
INSERT INTO `classes` VALUES ('大学物理', '星期四', '08:00:00', '否');
INSERT INTO `classes` VALUES ('线性代数', '星期五', '08:00:00', '否');
INSERT INTO `classes` VALUES ('JAVA程序设计', '星期五', '10:10:00', '否');
INSERT INTO `classes` VALUES ('数字逻辑', '星期四', '14:00:00', '否');
INSERT INTO `classes` VALUES ('初级法语', '星期三', '16:10:00', '否');
INSERT INTO `classes` VALUES ('初级日语', '星期五', '16:10:00', '否');
INSERT INTO `classes` VALUES ('艺术鉴赏', '星期二', '16:10:00', '否');
INSERT INTO `classes` VALUES ('音乐鉴赏', '星期四', '16:10:00', '否');
INSERT INTO `classes` VALUES ('舞蹈鉴赏', '星期三', '16:10:00', '否');
INSERT INTO `classes` VALUES ('职业规划', '星期三', '16:10:00', '否');
INSERT INTO `classes` VALUES ('高等数学', '星期一', '08:00:00', '否');
INSERT INTO `classes` VALUES ('概率论', '星期三', '08:00:00', '否');
INSERT INTO `classes` VALUES ('Python程序设计', '星期三', '10:10:00', '否');
INSERT INTO `classes` VALUES ('算法设计', '星期四', '10:10:00', '否');
INSERT INTO `classes` VALUES ('离散数学', '星期二', '10:10:00', '否');
INSERT INTO `classes` VALUES ('C语音程序设计', '星期二', '08:00:00', '否');
INSERT INTO `classes` VALUES ('网球', '星期二', '10:10:00', '否');
INSERT INTO `classes` VALUES ('乒乓球', '星期四', '10:10:00', '否');
INSERT INTO `classes` VALUES ('篮球', '星期三', '16:10:00', '否');

SET FOREIGN_KEY_CHECKS = 1;
