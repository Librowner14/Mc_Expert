# 麦当劳 MCP 接入说明

## 使用的 MCP Server

- Server：麦当劳 MCP Server
- 用途：查询餐品、价格及门店可售状态

## 使用的 Tool

示例 Tool 名称如下，实际名称以官方 MCP 文档为准：

- `search_menu_items`：按关键词、品类或预算查询餐品
- `get_item_detail`：获取餐品详情
- `check_store_availability`：查询指定门店的可售状态

## 调用流程

1. 用户输入用餐场景、预算和口味偏好。
2. Skill 解析用户条件并调用 `search_menu_items`。
3. 对候选餐品调用 `get_item_detail` 获取详情。
4. 如用户指定门店，则调用 `check_store_availability`。
5. Skill 按匹配程度生成推荐结果，并向用户说明推荐理由。

## 业务价值

该 Skill 将自然语言需求转换为菜单查询条件，降低用户选择餐品的时间成本，同时帮助用户在预算、口味和门店供应之间快速找到合适方案。

## 安全说明

MCP Token 仅通过环境变量传入，不写入代码或 Git 仓库；示例配置中不包含任何真实凭据。
