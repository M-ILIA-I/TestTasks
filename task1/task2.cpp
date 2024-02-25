#include <iostream>
#include <memory>
#include <vector>

class Widget {
public:
    Widget() : parent(nullptr) {}

    void setParent(std::shared_ptr<Widget> newParent) {
        parent = std::move(newParent);
    }

    std::shared_ptr<Widget> getParent() const {
        return parent;
    }

    virtual std::string getType() const {
        return "Widget";
    }

private:
    std::shared_ptr<Widget> parent;
};

class TabWidget : public Widget {
public:
    std::string getType() const override {
        return "TabWidget";
    }
};

class CalendarWidget : public Widget {
public:
    std::string getType() const override {
        return "CalendarWidget";
    }
};

int main() {
    std::shared_ptr<Widget> widget1 = std::make_shared<Widget>();
    std::shared_ptr<Widget> widget2 = std::make_shared<TabWidget>();
    std::shared_ptr<Widget> widget3 = std::make_shared<CalendarWidget>();

    widget2->setParent(widget1);
    widget3->setParent(widget1);

    std::cout << "Widget 1 Type: " << widget1->getType() << std::endl;
    std::cout << "Widget 2 Type: " << widget2->getType() << std::endl;
    std::cout << "Widget 3 Type: " << widget3->getType() << std::endl;

    return 0;
}