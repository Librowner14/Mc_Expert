"""麦麦营养搭配助手示例入口。

当前文件提供可运行的演示逻辑。接入正式麦当劳 MCP 后，可将
recommend() 中的示例菜单替换为 MCP Tool 的实时查询结果。
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class MenuItem:
    name: str
    price: float
    tags: tuple[str, ...]


SAMPLE_MENU = (
    MenuItem("麦辣鸡腿堡套餐", 35.0, ("午餐", "晚餐", "鸡肉", "辣")),
    MenuItem("板烧鸡腿堡套餐", 38.0, ("午餐", "晚餐", "鸡肉", "不辣")),
    MenuItem("猪柳蛋麦满分套餐", 28.0, ("早餐", "猪肉", "不辣")),
)


def recommend(scene: str, budget: float, preference: str = "") -> MenuItem | None:
    """按照场景、预算和口味，从示例菜单中选择一个餐品。"""
    candidates = [
        item
        for item in SAMPLE_MENU
        if item.price <= budget
        and scene in item.tags
        and (not preference or preference in item.tags)
    ]
    return min(candidates, key=lambda item: item.price, default=None)


def main() -> None:
    parser = argparse.ArgumentParser(description="根据场景和预算推荐麦当劳餐品")
    parser.add_argument("--scene", required=True, help="例如：早餐、午餐或晚餐")
    parser.add_argument("--budget", required=True, type=float, help="预算金额，单位：元")
    parser.add_argument("--preference", default="", help="例如：鸡肉、辣或不辣")
    args = parser.parse_args()

    item = recommend(args.scene, args.budget, args.preference)
    if item is None:
        print("暂未找到符合条件的餐品，请调整预算或偏好。")
        return

    print(f"推荐：{item.name}")
    print(f"预计价格：{item.price:.2f} 元")
    print("推荐理由：符合用餐场景、预算和口味条件。")


if __name__ == "__main__":
    main()
