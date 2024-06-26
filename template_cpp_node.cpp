#include "rclcpp/rclcpp.hpp"

class AddTwoIntsClientNode : public rclcpp::Node // MODIFY NAME
{
public:
    AddTwoIntsClientNode() : Node("node_name") // MODIFY NAME
    {
    }

private:
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddTwoIntsClientNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
