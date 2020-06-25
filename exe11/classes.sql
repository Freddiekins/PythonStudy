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

 Date: 25/06/2020 13:07:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for classes
-- ----------------------------
DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes`  (
  `num` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `time` time(0) NOT NULL,
  `is_selected` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classes
-- ----------------------------
INSERT INTO `classes` VALUES ('001', '计算机组成结构', '星期二', '08:00:00', '是');
INSERT INTO `classes` VALUES ('002', '数据库原理', '星期一', '08:00:00', '否');
INSERT INTO `classes` VALUES ('003', '软件工程', '星期二', '10:10:00', '是');
INSERT INTO `classes` VALUES ('004', '编译技术', '星期三', '14:00:00', '是');
INSERT INTO `classes` VALUES ('005', '大学物理', '星期四', '08:00:00', '否');
INSERT INTO `classes` VALUES ('006', '线性代数', '星期五', '08:00:00', '否');
INSERT INTO `classes` VALUES ('007', 'JAVA程序设计', '星期五', '10:10:00', '是');
INSERT INTO `classes` VALUES ('008', '数字逻辑', '星期四', '14:00:00', '否');
INSERT INTO `classes` VALUES ('009', '初级法语', '星期三', '16:10:00', '否');
INSERT INTO `classes` VALUES ('010', '初级日语', '星期五', '16:10:00', '否');
INSERT INTO `classes` VALUES ('011', '艺术鉴赏', '星期二', '16:10:00', '否');
INSERT INTO `classes` VALUES ('012', '音乐鉴赏', '星期四', '16:10:00', '否');
INSERT INTO `classes` VALUES ('013', '舞蹈鉴赏', '星期三', '16:10:00', '否');
INSERT INTO `classes` VALUES ('014', '职业规划', '星期三', '16:10:00', '是');
INSERT INTO `classes` VALUES ('015', '高等数学', '星期一', '08:00:00', '否');
INSERT INTO `classes` VALUES ('016', '概率论', '星期三', '08:00:00', '否');
INSERT INTO `classes` VALUES ('017', 'Python程序设计', '星期三', '10:10:00', '是');
INSERT INTO `classes` VALUES ('018', '算法设计', '星期四', '10:10:00', '否');
INSERT INTO `classes` VALUES ('019', '离散数学', '星期二', '10:10:00', '否');
INSERT INTO `classes` VALUES ('020', 'C语音程序设计', '星期二', '08:00:00', '否');
INSERT INTO `classes` VALUES ('021', '网球', '星期二', '10:10:00', '否');
INSERT INTO `classes` VALUES ('022', '乒乓球', '星期四', '10:10:00', '是');
INSERT INTO `classes` VALUES ('023', '篮球', '星期三', '16:10:00', '否');

SET FOREIGN_KEY_CHECKS = 1;
